This repository uses resources developed by the following authors:
* OpenSubtitles (opensubtitles.org)
* Text-SRT-Align - Jorg Tiedemann
* Serial Speakers dataset


## Instructions
1. Paste the export from OpenSubtitles (`.tar`) to the root of this directory
2. Run the following commands in bash:
`tar -xvf <export_name>`
`mv files/* opensubs`
`rmdir files`
`cd opensubs`
`gunzip export.txt.gz`

3. To extract the subtitles, navigate to the root of this directory and run `python extractor.py`
Subtitles will be contained in paths: IMDBID/lang/subtitle_file


## Pipeline
#### Preparing .txt subtitle files
Given .srt files obtained from OpenSubtitles:
1. `fix_encoding.sh` fixes all encodings of sub files using `enca` and `iconv` [NO NEED FOR CHINESE]
2. `convert_to_xml.sh` takes .srt files and converts them to .xml files using `srt2xml`
3. `align.sh` takes .xml files and aligns them using `srtalign` producing:
    - `$target_name.align` - alignment file per sub file
    - `corpus.align`: file which contains overlap values for all subtitle files 
4. `rank_alignments` takes the list from `corpus.align` and extracts the best subtitle file (=highest overlap) for each episode. The list of so selected files goes to `sub.paths`
5. `filter.sh` takes `sub.paths` and removes all .srt, .xml and .align files that aren't on the list
6. `generate_txt_wrapper.sh` fires `generate_txt.py` on every alignment file to generate .txt files.
7. `corpus_clean` is a folder containing relevant files categorised by episode.
