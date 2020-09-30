from dnachisel import *
import collections
from Bio.Align.Applications import MuscleCommandline as MCL
def generate_sequence_alignment(filename,muscle_exe):
    # from Bio.Align.Applications import MuscleCommandline as MCL
    muscle_cline = MCL(muscle_exe,input=filename)
    stdout, stderr = muscle_cline()
    text = stdout.split(">")
    newdict = {}
    for item in text[1:]:
        newlist = item.split("\n")
        header = newlist[0].strip()
        seq = "".join(newlist[1:]).strip().replace(" ","")
        newdict[header] = seq
    return newdict


def generate_consensus_sequence(seqdict):
    # import collections
    newtup = tuple(seqdict.items())
    sequence_list = [item[1] for item in newtup]
    final_sequence1 = []
    final_sequence2 = []
    for i in range(len(sequence_list[0])):
        sublist = [item[i] for item in sequence_list]
        counterobj = collections.Counter(sublist).most_common(2)
        if len(counterobj)>1 and counterobj[1][0] == "-":
            final_sequence1.append(counterobj[0][0])
            final_sequence2.append(counterobj[1][0])
        else:
            final_sequence1.append(counterobj[0][0])
            final_sequence2.append(counterobj[0][0])
    final_sequence1 = "".join(final_sequence1)
    final_sequence2 = "".join(final_sequence2)
    if final_sequence1 == final_sequence2:
        return final_sequence1
    else:
        return [final_sequence1,final_sequence2]


def codon_optimize_protein(aa_seq, species):
    # from dnachisel import *
    sequence = reverse_translate(aa_seq)
    species_dict = {"E. coli":"e_coli","B. subtilis":"b_subtilis","C. elegans":"c_elegans",
               "D. melanogaster":"d_melanogaster","G. gallus":"g_gallus",
               "H. sapiens":"h_sapiens","M. musculus":"m_musculus",
               "S. cerevisiae":"s_cerevisiae"}
    species = species_dict[species]
    problem = DnaOptimizationProblem(
    sequence=sequence,
    constraints=[EnforceGCContent(mini=0.3, maxi=0.7, window=50),
                 EnforceTranslation()],
    objectives=[CodonOptimize(species)])
    problem.resolve_constraints()
    problem.optimize()
    final_sequence = problem.sequence  # string
    final_record = problem.to_record(with_sequence_edits=True)
    return final_sequence

def align_and_optimize_protein():
    muscle_exe = r"D:\Downloads\muscle3.8.31_i86win32.exe"
    in_file = "unaligned4.fasta"
    seqdict = generate_sequence_alignment(in_file,muscle_exe)
    final_seq = generate_consensus_sequence(seqdict)
    if type(final_seq) == list:
        newseq = final_seq[0]
    else:
        newseq =final_seq
    codon_optimized_seq = codon_optimize_protein(newseq,"E. coli")
    return codon_optimized_seq

def write_input_to_file(input_list):
    newfile = open("input.fasta","w")
    newstr = ""
    for i in range(len(input_list)):
        if i%2 == 0:
            newstr += "> "
            newstr += input_list[i].text().strip()
            newstr += "\n"
        else:
            newstr += input_list[i].toPlainText().strip()
            newstr += "\n"
    newfile.write(newstr)
    newfile.close()
    return newstr

