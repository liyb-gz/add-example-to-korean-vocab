import os
import math
import json
import time
import requests
from typing import List, Dict, Optional
from config import API_KEY, API_URL, MODEL

def read_vocabulary_file(filename: str) -> List[str]:
    """Read the vocabulary file and return list of lines."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()

def read_prompt_template(filename: str) -> str:
    """Read the prompt template file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def split_into_groups(vocab_lines: List[str], group_size: int = 30) -> List[List[str]]:
    """Split vocabulary lines into groups of specified size."""
    return [vocab_lines[i:i + group_size] for i in range(0, len(vocab_lines), group_size)]

def get_completion(prompt: str) -> Optional[str]:
    """Get completion from OpenRouter API."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error getting completion: {e}")
        return None

def process_group(vocab_group: List[str], prompt_template: str) -> List[str]:
    """Process a group of vocabulary words using the AI."""
    # Create prompt by inserting vocab group into template
    prompt = prompt_template.replace("{vocab_list}", "".join(vocab_group))
    
    # Get completion from API
    result = get_completion(prompt)
    
    if result:
        # Print raw result for debugging
        print(result)
        
        # Extract content between <processed_list> tags
        if "<processed_list>" in result and "</processed_list>" in result:
            start_idx = result.find("<processed_list>") + len("<processed_list>")
            end_idx = result.find("</processed_list>")
            result = result[start_idx:end_idx].strip()
            
            # Split into lines and filter out empty lines
            return [line for line in result.split('\n') if line.strip()]
    return []

def save_progress(filename: str, processed_lines: List[str]):
    """Save processed lines to a progress file."""
    with open(filename, 'w', encoding='utf-8') as f:
        for line in processed_lines:
            line = line.rstrip('\n')  # Remove any existing newlines
            f.write(f"{line}\n")  # Add single newline

def load_progress(filename: str) -> List[str]:
    """Load previously processed lines."""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            # Read lines and strip any trailing whitespace/newlines
            return [line.rstrip('\n') for line in f.readlines()]
    return []

def main():
    # Input and output files
    vocab_file = "vocab.tsv"
    prompt_file = "prompt.md"
    progress_file = "progress.tsv"
    
    # Read input files
    vocab_lines = read_vocabulary_file(vocab_file)
    prompt_template = read_prompt_template(prompt_file)
    
    # Load previous progress if exists
    processed_lines = load_progress(progress_file)
    start_index = len(processed_lines)
    
    # Split remaining vocabulary into groups
    remaining_lines = vocab_lines[start_index:]
    groups = split_into_groups(remaining_lines)
    
    print(f"Starting from index {start_index}, {len(groups)} groups to process")
    
    # Process each group
    for i, group in enumerate(groups):
        print(f"Processing group {i+1}/{len(groups)}")
        
        # Process group and get results
        result_lines = process_group(group, prompt_template)
        
        if result_lines:
            # Add new results to processed lines
            processed_lines.extend(result_lines)
            
            # Save progress after each group
            save_progress(progress_file, processed_lines)
            
            # Wait between requests to avoid rate limits
            time.sleep(2)
        else:
            print(f"Failed to process group {i+1}, stopping")
            break
    
    # Save final output
    with open("vocab_with_examples.tsv", 'w', encoding='utf-8') as f:
        for line in processed_lines:
            line = line.rstrip('\n')  # Remove any existing newlines
            f.write(f"{line}\n")  # Add single newline

if __name__ == "__main__":
    main()
