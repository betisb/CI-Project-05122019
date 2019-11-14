# Remove Any Docker installation
sudo apt-get remove docker docker-engine docker.io containerd runc
#update the repo
sudo apt-get update
#install prerequirments
sudo apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common

#Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
#verify
sudo apt-key fingerprint 0EBFCD88
#Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below. Learn about nightly and test channels.
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

#Update the apt package index
sudo apt-get update
#Install the latest version of Docker Engine - Community and containerd, or go to the next step to install a specific version
sudo apt-get -y install docker-ce docker-ce-cli containerd.io
#test docker
sudo docker run hello-world
sudo passwd root
#some password for root
#switch to root user
su -

docker pull biocontainers/blast:v2.2.31_cv2
docker run biocontainers/blast:v2.2.31_cv2 blastp -help
mkdir blast_example
cd blast_example
wget http://www.uniprot.org/uniprot/P04156.fasta
curl -O ftp://ftp.ncbi.nih.gov/refseq/D_rerio/mRNA_Prot/zebrafish.1.protein.faa.gz
gunzip zebrafish.1.protein.faa.gz
docker run -v `pwd`:/data/ biocontainers/blast:v2.2.31_cv2 makeblastdb -in zebrafish.1.protein.faa -dbtype prot
docker run -v `pwd`:/data/ biocontainers/blast:v2.2.31_cv2 blastp -query P04156.fasta -db zebrafish.1.protein.faa -out results.txt
less results.txt