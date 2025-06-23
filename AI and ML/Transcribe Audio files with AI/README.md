<img src="https://cdn.prod.website-files.com/677c400686e724409a5a7409/6790ad949cf622dc8dcd9fe4_nextwork-logo-leather.svg" alt="NextWork" width="300" />

# Transcribe Audio Files with AI

**Project Link:** [View Project](http://learn.nextwork.org/projects/aws-ai-transcribe)

**Author:** Kareshma Rajaananthapadmanaban  
**Email:** kareshma2909@gmail.com

---

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-ai-transcribe_o2p3q4r1)

---

## Introducing Today's Project!

In this project, I will demonstrate how to use Amazon Transcribe to convert audio and video files into readable, searchable text. I'm doing this project to learn how AWS AI services can process audio data efficiently, making it useful for applications like subtitles, blogs, and voice commands.

### Tools and concepts

Services I used were Amazon S3 for storing media files and Amazon Transcribe for converting audio to text. Key concepts I learnt include creating and applying custom vocabularies to improve term recognition, using vocabulary filters to remove unwanted words, and enabling features like real-time transcription, speaker partitioning, and subtitle generation.

### Project reflection

This project took me approximately 1 hour to complete the hands-on tasks and an extra 30 minutes for writing and refining the documentation. The most challenging part was configuring and testing the custom vocabulary and filters to see their effect in real-time transcription. It was most rewarding to see how these customizations improved the transcription output.

I did this project today to gain hands-on experience with Amazon Transcribe and understand how to improve audio transcription using custom vocabularies, filters, and real-time streaming. This project met my goals by teaching me practical skills for processing audio data in AWS and showing how AI-powered transcription can be customized for better accuracy and usability.

---

## S3 and Transcribe

To set up for this project, I'm using an S3 bucket to store the video file because Amazon Transcribe requires media files to be stored in an S3 bucket for processing. The file I'm transcribing is 1-min-clip.mp4, which I downloaded and verified on my local machine before uploading it to the newly created S3 bucket for use in transcription tasks.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-ai-transcribe_k1l4m7n0)

---

## Run A Transcription Job

The steps to run a transcription job include creating an S3 bucket, uploading the audio file, accessing the Amazon Transcribe console, setting job details like name, model type, and selecting the input file from S3. Overall, this process took me around 10–15 minutes, including setup and waiting for the transcription job to complete.

Amazon Transcribe uses model types to determine how audio is converted into text using AI-powered machine learning models. Use cases of model types include handling general conversations with the General model or improving accuracy for specific industries like medical or legal with custom models trained on domain-specific data and vocabulary.

You can customize a transcription further with subtitling, which adds SRT subtitle files to make videos accessible to wider audiences, and speaker partitioning, which helps to identify and separate different speakers in the transcript. This makes it easier to understand multi-speaker conversations and improves transcript readability by labeling who said what.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-ai-transcribe_g0h1i2j3)

---

## Baseline Transcript Review

To start using Amazon Transcribe, I first ran a baseline transcription job, which means processing the audio file without any custom vocabularies, filters, or advanced settings. This is because a baseline helps me understand how well Transcribe performs with raw audio by default, giving a reference point to measure improvements when I apply enhancements later.

While reviewing the baseline transcript, I noticed minor inaccuracies such as misinterpreted words, missing punctuation, and slight errors in recognizing jargon or unclear speech. These happened because the General model may not fully capture domain-specific terms or handle background noise perfectly without custom vocabularies or filters applied.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-ai-transcribe_s3t6u9v2)

---

## Custom Vocabulary

I can resolve transcription inaccuracies using a custom vocabulary, which is a list of specific words or phrases that I want Amazon Transcribe to recognize correctly. A custom vocabulary improves transcription accuracy by teaching Transcribe how to handle unique terms, technical jargon, brand names, or uncommon phrases that aren't well understood by its general language model.

To create an item in a custom vocabulary, you need to define two values. They are the Phrase, which tells Amazon Transcribe the word or term to recognize in the audio, and DisplayAs, which defines how that word should appear in the transcript. For example, entering “player” as the Phrase and “Player” as DisplayAs ensures correct capitalization in the output.

My custom vocabulary defines specific terms to improve transcription accuracy. It includes "player" displayed as "Player," correcting the typo "repositoriesies" to "repositories," and fixing "four-or-three-forbidden" to "403 Forbidden." These updates ensure that Amazon Transcribe properly recognizes and displays these important words in the final transcript.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-ai-transcribe_e3f4g5h6)

---

## Vocabulary Filters

Another feature in Transcribe is vocabulary filtering, which removes or masks unwanted words or phrases during transcription, such as filler words or sensitive terms. It's different from custom vocabularies because filters exclude or hide words, while custom vocabularies help Transcribe recognize and correctly transcribe specific or uncommon words.

My vocabulary filter removes common filler words like "uh," "um," and "like" to make the transcript sound clearer and more professional. To set up this filter, I first created a plain text file named filler-words-filter.txt in Notepad, listing these unwanted words separated by commas. This file is then uploaded to Amazon Transcribe as a vocabulary filter.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-ai-transcribe_u7v8w9x0)

---

## Enhanced Transcription

### I ran a new transcription with my custom vocabulary and filtering settings

The enhanced transcription is better than the baseline because it accurately recognized key terms from the custom vocabulary and removed unwanted filler words using the vocabulary filter. This made the transcript clearer and more professional. However, some terms like "403 Forbidden" still need improvement, showing that further customization or model training may be needed.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-ai-transcribe_k1l2m3n4)

---

## Real Time Transcription

For my project extension, I experimented with real-time transcription, which converts spoken words into text instantly as the speaker talks. This feature is ideal for applications like live captioning, virtual assistants, or real-time customer support tools, where immediate speech-to-text conversion enhances user experience and accessibility.

Even during real-time transcription, I could use features like custom vocabulary and vocabulary filtering to improve accuracy. Overall, compared to a transcription job, real-time transcription was impressive but slightly less accurate, especially with complex terms like “403 Forbidden,” showing that real-time processing may need further tuning for perfect results.Services I used were Amazon S3 for storing media files and Amazon Transcribe for converting audio to text. Key concepts I learnt include creating and applying custom vocabularies to improve term recognition, using vocabulary filters to remove unwanted words, and enabling features like real-time transcription, speaker partitioning, and subtitle generation.

![Image](http://learn.nextwork.org/easygoing_white_heroic_bilberry/uploads/aws-ai-transcribe_a5b6c7d8)

---

---
