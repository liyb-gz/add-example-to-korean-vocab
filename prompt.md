<Input Variables>
vocab_list
</Input Variables>

<Instructions Structure>
1. Define the column structure
2. Show the input TSV format
3. Explain what we want to do with each row 
4. Specify output format requirements and bold formatting
5. Provide detailed guidelines for example sentence creation
6. Show clear examples with various conjugations
</Instructions Structure>

<Instructions>
You will be helping to enhance a Korean vocabulary list by adding appropriate example sentences and their English translations. You will receive a TSV (tab-separated values) formatted list of Korean vocabulary words. Each row in the list contains the following columns in order:
1. Korean: The vocabulary word in Korean
2. English: English translation(s)
3. Hanja: Chinese characters (if applicable)
4. Audio: Reference to audio file
5. Example Sentence: Korean example sentence (this is what you'll be adding)
6. Example Sentence Translation: English translation of the example sentence (this is what you'll be adding)
7. ID: Unique identifier number

<vocab_list>
{vocab_list}
</vocab_list>

For each word, create a natural Korean example sentence that clearly demonstrates the word's usage, along with an accurate English translation. The target word in each example sentence should be wrapped in <b> tags for bold formatting.

Follow these guidelines for creating example sentences:

For verbs and adjectives:
- Use various forms and conjugations, include but not limited to:
  * Present tense (해요/합니다)
  * Past tense (했어요/했습니다)
  * Future tense (할 거예요/하겠습니다)
  * Want to do (-고 싶어요)
  * Please do (~해 주세요)
  * Let's do (~합시다)
  * Must do (~해야 해요)
  * Can do (~할 수 있어요)
- Mix both polite and formal levels of speech
- Include both positive and negative forms where appropriate

For nouns and other parts of speech:
- Keep sentences concise but clear (typically 3-7 words)
- Use common vocabulary in the surrounding context
- Show the word in its most typical usage

Examples of appropriate sentences with varied conjugations and translations:
- For "네" (yes):
  Korean: "<b>네</b>, 알겠습니다."
  English: "Yes, I understand."
- For "있다" (to exist/have):
  * Present:
    Korean: "책이 여기 <b>있어요</b>."
    English: "The book is here."
  * Want to:
    Korean: "집에 <b>있고 싶어요</b>."
    English: "I want to be at home."
  * Must:
    Korean: "도서관에 <b>있어야 해요</b>."
    English: "I must be at the library."
- For "학교" (school):
  Korean: "<b>학교</b>에 가고 싶어요."
  English: "I want to go to school."
- For "집" (house):
  Korean: "우리 <b>집</b>은 작아요."
  English: "Our house is small."

Format your output in TSV format, maintaining the exact same structure as the input. Include all original data exactly as provided, only adding content in the "Example Sentence" column (5th column) and "Example Sentence Translation" column (6th column). Preserve:
- Tab separation between fields
- Line breaks between entries
- The order of entries
- ID numbers

Wrap the processed list in <processed_list> tags. Do not include the header row in your output.

Example of expected output format:
<processed_list>
네	yes	네	[sound:yes.mp3]	<b>네</b>, 알겠습니다.	Yes, I understand.	1
(and so on...)
</processed_list>