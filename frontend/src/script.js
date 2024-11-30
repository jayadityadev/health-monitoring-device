const searchInput = document.getElementById("search-patient");
const autocompleteList = document.getElementById("autocomplete-list");
const addPatientButton = document.getElementById("add-patient-btn");
const patientForm = document.getElementById("patient-form"); // Corrected line
const addPatientForm = document.getElementById("add-patient-form");
const patientList = document.getElementById("patient-list");

let patients = [];

// Function to fetch patient data from the API
async function fetchPatients() {
    try {
        const response = await fetch("http://localhost:8000/patients_data");
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        patients = await response.json();
        displayPatients();
    } catch (error) {
        console.error("There was a problem with the fetch operation:", error);
    }
}

// Function to display patients
function displayPatients() {
    patientList.innerHTML = '';
    patients.forEach(patient => {
        const patientDiv = document.createElement("div");
        patientDiv.className = "patient-details";
        patientDiv.innerHTML = `
            <p><strong>Patient Name:</strong> ${patient.name}</p>
            <p><strong>Age:</strong> ${patient.age}</p>
            <p><strong>Sex:</strong> ${patient.sex}</p>
            <p><strong>Weight:</strong> ${patient.weight} kg</p>
            <p><strong>Blood Group:</strong> ${patient.blood_group}</p>
            <button class="details-btn" id="${patient.id}"><a href="index02.html">Details</a></button>
        `;
        patientList.appendChild(patientDiv);
    });
}

// Function to add a patient
async function addPatient(patientData) {
    try {
        const response = await fetch("http://localhost:8000/patients_data", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(patientData)
        });

        if (!response.ok) {
            throw new Error("Failed to add patient");
        }

        const newPatient = await response.json();
        patients.push(newPatient);
        displayPatients(); // Refresh the patient list
        patientForm.classList.add('hidden'); // Hide the form after submission
    } catch (error) {
        console.error("Error adding patient:", error);
    }
}

// Add patient form submission
addPatientForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const patientData = {
        name: document.getElementById("patient-name").value,
        sex: document.getElementById("patient-sex").value,
        height: parseInt(document.getElementById("height").value),
        weight: parseFloat(document.getElementById("weight").value),
        age: parseInt(document.getElementById("age").value),
        blood_group: document.getElementById("patient-bloodgroup").value,
    };

    addPatient(patientData);
    addPatientForm.reset(); // Reset the form after submission
});

// Show the patient form when the button is clicked
addPatientButton.addEventListener("click", () => {
    patientForm.classList.toggle('hidden');
});

// Search functionality
searchInput.addEventListener("input", () => {
    const query = searchInput.value.toLowerCase();
    autocompleteList.innerHTML = "";

    if (query) {
        const filteredPatients = patients.filter(patient =>
            patient.name.toLowerCase().includes(query) || patient.id.toLowerCase().includes(query)
        );

        filteredPatients.forEach(patient => {
            const item = document.createElement("div");
            item.className = "autocomplete-item";
            item.textContent = `${patient.name} (${patient.id})`;
            item.addEventListener("click", () => {
                searchInput.value = `${patient.name} (${patient.id})`;
                autocompleteList.innerHTML = ""; // Clear suggestions
            });
            autocompleteList.appendChild(item);
        });
    }
});

// Initial fetch of patients
fetchPatients();