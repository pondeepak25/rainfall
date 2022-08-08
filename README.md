// build the image
docker build -t rainfall .

// list the image
docker images

//run
docker run -d -p 5000:5000 rainfall

//check the running processes
docker ps

// login into your registry (Docker Hub)
docker login

// tag the image
docker tag rainfall pondeepak25/rainfall:latest

// push the image
docker push pondeepak25/rainfall:latest

//Enable Hyper-V
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

//set the driver

minikube config set driver hyperv

//start minikube

minikube start

// pull  the image
minikube image pull docker.io/pondeepak25/rainfall:latest

//create Deployment Config

kubectl create deployment rainfall --image=docker.io/pondeepak25/rainfall:latest

// create service
kubectl expose deployment rainfall --type=LoadBalancer --port=8080

//Access the service
minikube service rainfall --url

//port-forward
kubectl port-forward service/rainfall 8080:8080

//access the dashboard
minikube dashboard --url