
# Aarogya Sangraha

Aarogya Sangraha is a comprehensive healthcare platform designed to centralize and streamline various aspects of the healthcare ecosystem. This project aims to address the challenges faced in the fragmented healthcare system by providing a unified platform for administrators, medical practitioners, hospitals, and patients.

## Features

#### Admin User:
- Approves hospitals
- Takes actions on queries
- Handles medicines

#### Medical Practitioner:
- Sends job applications to hospitals
- Treats patients
- Nurses can add vitals

#### Hospital:
- Accepts doctors
- Tracks doctors' activities

#### Patient:
- Keeps history of vitals and treatments
- Can raise query against any treatment

#### Treatment Verification:
- Enables verification of treatment using treatment ID
- Accessible to both registered and unregistered users
## Run Locally

Clone the project

```bash
  git clone https://github.com/ishaan19d/AarogyaSangraha.git
```

Go to the project directory

```bash
  cd AarogyaSangraha
```

Install dependencies

```bash
  pip3 install Django==4.2
```

Start the server

```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
```

