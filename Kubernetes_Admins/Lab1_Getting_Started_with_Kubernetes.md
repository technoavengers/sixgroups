# Lab 1: Getting Started with Kubernetes

**Running MinIO as a Container on Docker**  
**Time:** 20 Minutes

## Lab Summary
This lab introduces the fundamental concepts of containerization. Participants will use a pre-installed Docker environment to pull a pre-built image from Docker Hub and run a basic containerized application.

## Objectives
- Pulling a Pre-Built Image from Docker Hub
- Running a Containerized Application
- Exploring Container Management
- Removing Containers
- Creating Your Own Docker Image

---

## Step 1: Pulling a Pre-Built Image from Docker Hub

1. **Open your terminal.**
   - Ensure Docker is installed by running:
     ```bash
     docker --version
     ```

2. **Pull the MinIO image from Docker Hub:**
   - Run the following command:
     ```bash
     docker pull minio/minio
     ```

3. **Verify the image is pulled:**
   - Check if the image is available locally:
     ```bash
     docker images
     ```

---

## Step 2: Running a Containerized MinIO Application

1. **Run the MinIO container:**
   - Start a MinIO container with the following command:
     ```bash
     docker run -d -p 9000:9000 -p 9001:9001 --name minio -e "MINIO_ROOT_USER=admin" -e "MINIO_ROOT_PASSWORD=password" minio/minio server /data --console-address ":9001"
     ```

   **Explanation:**
   - `docker run`: Base command to create and run a new container.
   - `-d`: Runs the container in detached mode (in the background).
   - `-p 9000:9000`: Maps port 9000 on the host to port 9000 in the container (used for S3 API access).
   - `-p 9001:9001`: Maps port 9001 on the host to port 9001 in the container (used for the MinIO web console).
   - `--name minio`: Assigns the name "minio" to the container.
   - `-e "MINIO_ROOT_USER=admin"`: Sets the root user to "admin".
   - `-e "MINIO_ROOT_PASSWORD=password"`: Sets the root password to "password".
   - `minio/minio`: Specifies the Docker image to use.
   - `server /data`: Command inside the container to start MinIO in server mode.
   - `--console-address ":9001"`: Sets the web console to port 9001.

2. **Check running containers:**
   - List all running containers to ensure MinIO is running:
     ```bash
     docker ps
     ```

3. **Access the MinIO Console:**
   - Open a web browser and navigate to [http://localhost:9001](http://localhost:9001).
   - Log in with the credentials:
     - Username: `admin`
     - Password: `password`

---

## Step 3: Exploring Container Management

1. **View container logs:**
   - Check the logs of the MinIO container:
     ```bash
     docker logs minio
     ```

2. **Access the container’s shell (optional):**
   - Start a shell session inside the container:
     ```bash
     docker exec -it minio /bin/bash
     ```
   - Run `ls` to explore the filesystem, then exit:
     ```bash
     ls
     exit
     ```

3. **Stop the MinIO container:**
   - Stop the container:
     ```bash
     docker stop minio
     ```

4. **Remove the MinIO container:**
   - Remove the container:
     ```bash
     docker rm minio
     ```

5. **Confirm deletion:**
   - Run `docker ps` again to confirm the container is no longer running:
     ```bash
     docker ps
     ```

---

## Step 4: Creating Your Own Docker Image

1. **Create a simple Dockerfile:**
   - Create a new directory and navigate to it:
     ```bash
     mkdir myminioapp
     cd myminioapp
     ```
   - Create and open a Dockerfile using the nano editor:
     ```bash
     nano Dockerfile
     ```
   - Add the following content and save:
     ```Dockerfile
     FROM minio/minio
     CMD ["minio", "server", "/data", "--console-address", ":9001"]
     ```

2. **Build the Docker image:**
   - Build the image with the following command:
     ```bash
     docker build -t myminioapp:latest .
     ```

3. **Check your custom image:**
   - Verify the image was created:
     ```bash
     docker images
     ```

4. **Run the newly created image:**
   - Test the image by running a container:
     ```bash
     docker run -d -p 9000:9000 -p 9001:9001 --name myminioapp -e "MINIO_ROOT_USER=admin" -e "MINIO_ROOT_PASSWORD=password" myminioapp
     ```

5. **Check your containers again:**
   - Confirm the new container is running:
     ```bash
     docker ps
     ```

6. **Access the MinIO Console:**
   - Navigate to [http://localhost:9001](http://localhost:9001) and log in with the same credentials.

---

## Conclusion
In this lab, you learned the basics of working with containers using MinIO as an example. You pulled the MinIO image from Docker Hub, ran MinIO as a containerized application, explored container management, and created your own Docker image. This foundational knowledge will help you leverage containerization for deploying and managing applications efficiently.

**END OF LAB**
