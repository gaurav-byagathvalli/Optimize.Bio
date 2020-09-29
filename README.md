# Optimize.Bio
A Consensus Sequence Design Tool for Molecular Cloning Workflows and DNA Vaccine Design

Optimize.Bio is a sequence alignment and codon optimization tool designed to create multiple sequence alignments (MSA) for input amino acid sequences and generate a codon-optimized cDNA sequence for molecular cloning. The purpose of this program is to rapidly generate optimized sequences to synthetically design and produce proteins to clone into expression plasmids. An example use case would be optimization of the SARS-CoV-2 Spike Protein sequence from different strains to generate a human-centered sequence for designing a DNA vaccine. Optimize.Bio is an easy-to-use desktop GUI supporting manual file inputs or file uploads and processing of between 3-10 amino acid sequences at a time. The MSA algorithm is derived from the [MUSCLE algorithm](https://biopython.org/docs/dev/api/Bio.Align.Applications.html) developed by Robert C. Edgar and included in the Biopython module (1). The codon optimization algorithm used here was developed by the Ediburgh Genome Foundry called [DNAChisel](https://github.com/Edinburgh-Genome-Foundry/DnaChisel), consisting of a massive library with different tools from which the DNA optimization and reverse translation tools were obtained (2). The consensus sequence design algorithm was developed by me, and is a relatively simple implementation relying on nucleotide frequencies within a given set of input sequences from the MSA. 

<p align="center">
  <img src="https://i.imgur.com/iXgN8dn.gif" />
</p>

# Usage
Under the main application:
1) Sequence Count: The number of sequences you wish to manually enter for processing. This value MUST be filled in to see the final output regardless of whether you are manually entering your sequences or not.
2) Input Method: The method through which you plan to enter your sequences. Manual will enable n number of sequence cells as specified under sequence count. File upload will allow you to select a FASTA file from your computer to upload. Your code MUST be in the correct FASTA format, otherwise the program will be unable to process your file.
3) Sequence Type: Currently, Optimize.Bio only supports amino acid sequences (protein sequences). Future work will include DNA sequences.
4) Desired Species: Select the species for which you would like codon optimization to be performed on (your final output DNA sequence will be codon optimized for this species.)
5) Sequence Labels: Enter Descriptive Labels for your appropriate sequences. These can be exported to a file (detailed below).
6) Sequence Text: Enter your amino acid sequences WITHOUT any spaces in between or at the ends. 

Under the main menu:
1) Export Current Output: Creates a .txt log file with the input sequences, output sequence, and date/time of file creation for tracking and external use.
2) Clear and Reset: Resets all settings to default (as if the application was just opened)


# Relevant Credit
1) Thanks to the Edinburgh Genome Foundry for developing DNAChisel, an incredibly powerful bioinformatics platform that continues to grow everyday. Take a look at DNAChisel [here](https://github.com/Edinburgh-Genome-Foundry/DnaChisel).
2) Thanks to Colin Duquesnoy for the QDarkStyleSheet used as the theme for this application. The stylesheet can be found [here](https://github.com/ColinDuquesnoy/QDarkStyleSheet/blob/master/qdarkstyle/style.qss).

# License = MIT
Optimize.Bio is an open-source software developed by me (Gaurav Byagathvalli) and released on GitHub under the MIT license. Feel free to contribute or suggest improvements!

# References 
1) Edgar R. C. (2004). MUSCLE: multiple sequence alignment with high accuracy and high throughput. Nucleic acids research, 32(5), 1792–1797. https://doi.org/10.1093/nar/gkh340
2) Zulkower, V., & Rosser, S. (2020). DNA Chisel, a versatile sequence optimizer. Bioinformatics (Oxford, England), btaa558. Advance online publication. https://doi.org/10.1093/bioinformatics/btaa558
