sudo docker pull biocontainers/blast:v2.2.31_cv2
sudo docker run biocontainers/blast:v2.2.31_cv2 blastp -help
mkdir blast_example
cd blast_example
wget http://www.uniprot.org/uniprot/P04156.fasta
curl -O ftp://ftp.ncbi.nih.gov/refseq/D_rerio/mRNA_Prot/zebrafish.1.protein.faa.gz
gunzip zebrafish.1.protein.faa.gz
sudo docker run -v `pwd`:/data/ biocontainers/blast:v2.2.31_cv2 makeblastdb -in zebrafish.1.protein.faa -dbtype prot
sudo docker run -v `pwd`:/data/ biocontainers/blast:v2.2.31_cv2 blastp -query P04156.fasta -db zebrafish.1.protein.faa -out results.txt
less results.txt