# hw02-module2
STEP 1
Run you own docker registry, create a volume and mount it as the registry folder, push images into it, stop container, start it again and confirm that you can pull images
![alt text](<screenshots/Знімок екрана з 2024-02-15 16-15-01.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-15 16-20-19.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-15 16-23-00.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-15 16-27-16.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-15 16-31-16.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-15 16-33-46.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-15 16-36-41.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-15 16-46-20.png>)

STEP 2
Tag image with different name, e.g. localhost:5000/python, push it to registry and confirm that it shows that layes already exist
![alt text](<screenshots/Знімок екрана з 2024-02-16 01-02-44.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-16 01-02-54.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-16 00-49-25.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-16 00-49-38.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-16 00-52-10.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-16 00-58-49.png>)

STEP 3
Add /healthz endpoint to python app which works in the same way like nodejs endpoint, optionally, add healthcheck to image using this endpoint
![alt text](<screenshots/Знімок екрана з 2024-02-16 22-59-27.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-16 23-00-24.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-16 23-04-28.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-16 23-05-16.png>)
![alt text](<screenshots/Знімок екрана з 2024-02-16 23-09-21.png>)