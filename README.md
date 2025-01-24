# Korean Vocabulary Example Sentence Generator

A Python script that uses AI to automatically generate natural Korean example sentences for vocabulary words.

## Overview

This tool takes a list of Korean vocabulary words in TSV format and enhances it by adding appropriate example sentences that demonstrate proper usage. By default it uses the OpenAI API with ChatGPT 4o to generate contextually appropriate sentences.

## Features

-   Processes vocabulary lists in TSV format
-   Generates natural Korean example sentences with proper conjugations
-   Handles various parts of speech (verbs, adjectives, nouns, etc.)
-   Maintains consistent formatting with bold tags for target words
-   Supports batch processing with progress tracking
-   Preserves original vocabulary data structure

## Input Format

The input vocabulary file should be a TSV file with the following columns:

1. Korean word
2. English translation(s)
3. Hanja (Chinese characters) if applicable
4. Audio file reference
5. Example sentence (will be populated)
6. Example sentence's English translation (will be populated)
7. ID number

## Usage

1. Create a file named `vocab.tsv` with your vocabulary list in TSV format
2. Set up your OpenAI API key and API URL in `config.py`
3. Run the script: `python add_example_sentence.py`
4. The output will be saved as `vocab_with_examples.tsv`
