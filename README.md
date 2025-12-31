

# Contacts API (MongoDB)

This application exposes a simple REST API that connects to a MongoDB data server and manages contact information.

## Data Model

Each contact is stored in the following structure:

```json
{
  "first_name": "name",
  "last_name": "name",
  "phone_number": "phone_number"
}
```

## API Endpoints

### 1. Get All Contacts

* **Method:** `GET`
* **Endpoint:** `/contacts`
* **Description:** Returns all contacts found in the database.

---

### 2. Add a New Contact

* **Method:** `POST`
* **Endpoint:** `/contacts`
* **Description:** Adds a new contact to the database.
* **Requirements:** All fields are mandatory.

**Request Body Example:**

```
first_name: <name>
last_name: <name>
phone_number: <phone_number>
```

---

### 3. Update an Existing Contact

* **Method:** `PUT`
* **Endpoint:** `/contacts/{id}`
* **Description:** Updates an existing contact by ID.
* **Notes:** Include only the fields you want to update in the request body.

**Example URL:**

```
http://127.0.0.1:50287/contacts/<id>
```

> The port may differ in your environment.

---

### 4. Delete a Contact

* **Method:** `DELETE`
* **Endpoint:** `/contacts/{id}`
* **Description:** Deletes a contact by ID.

**Example URL:**

```
http://127.0.0.1:50287/contacts/<id>
```

## Running the Application

### Prerequisites

* `kubectl` installed
* `minikube` installed and running

### Steps

1. Open a command prompt / terminal.
2. Navigate to the project’s `software` folder.
3. Apply the Kubernetes configuration:

   ```bash
   kubectl apply -f ./k8s
   ```
4. Expose the service using Minikube:

   ```bash
   minikube service api-service
   ```

This command will open the application in your default browser.

---

## Notes

* Make sure MongoDB is accessible from the cluster.
* Ports and service URLs may vary depending on your local setup.
