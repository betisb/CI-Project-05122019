export PROJECT_ID='[PROJECT_ID]'

gcloud iam service-accounts create ssh-account --project $PROJECT_ID \
   --display-name "ssh-account"

gcloud compute networks create ssh-example --project $PROJECT_ID

gcloud compute firewall-rules create ssh-all --project $PROJECT_ID \
   --network ssh-example --allow tcp:22

gcloud compute instances create target --project $PROJECT_ID \
   --zone us-central1-f --network ssh-example \
   --no-service-account --no-scopes \
   --machine-type f1-micro --metadata=enable-oslogin=TRUE

gcloud compute instances add-iam-policy-binding target \
   --project $PROJECT_ID --zone us-central1-f \
   --member serviceAccount:ssh-account@$PROJECT_ID.iam.gserviceaccount.com \
   --role roles/compute.osAdminLogin

gcloud compute instances create source \
   --project $PROJECT_ID --zone us-central1-f \
   --service-account ssh-account@$PROJECT_ID.iam.gserviceaccount.com  \
   --scopes https://www.googleapis.com/auth/cloud-platform \
   --network ssh-example --machine-type f1-micro

gcloud compute ssh source --project $PROJECT_ID --zone us-central1-f