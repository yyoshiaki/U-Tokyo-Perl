from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

fasta_file = './samples/sample_amino.fasta'
print('Opening FASTA files...')
handle = open(fasta_file, "rU")
records = list(SeqIO.parse(handle, "fasta"))
handle.close()
print('Got these sequences.')
for record in records:
    print(record.id)

print('\nDoing the BLAST and retrieving the results...')
files = []
for record in records:
    print(record.id)
    result_handle = NCBIWWW.qblast('blastp', 'nr', record.seq)

    # save the results for later, in case we want to look at it
    # fastaのIDを｜で区切って最後の要素をファイル名に使用している。
    # ファイル名のルールを変えたいときはフレキシブルに。
    current_file = './results/blast_' + record.id.split('|')[-1] + '.xml'
    save_file = open(current_file, 'w')
    files.append(current_file)
    blast_results = result_handle.read()
    save_file.write(blast_results)
    save_file.close()
    print('File was successfully saved.\n')


for file in files:
    print(records[2].id)
    result_handle = open(file, 'r')
    # クエリ配列が一つの時はこれ。
    #blast_record = NCBIXML.read(result_handle)
    blast_records = NCBIXML.parse(result_handle)

    for blast_record in blast_records:
        # 2番めに似たアラインメントを取り出す。
        alignment = blast_record.alignments[1]
        for hsp in alignment.hsps:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')