
const API_URL = "http://127.0.0.1:8000";

async function checkBackend() {
    const status = document.getElementById("apiStatus");

    try {
        const response = await fetch(`${API_URL}/health`);

        if (!response.ok) {
            throw new Error("Backend request failed");
        }

        const data = await response.json();

        status.textContent =
            `● API CONNECTED — ${data.status.toUpperCase()}`;

        status.style.color = "#10b981";

    } catch (error) {
        status.textContent = "● API DISCONNECTED — Check backend";

        status.style.color = "#ef4444";

        console.error(error);
    }
}

document.getElementById("askButton").addEventListener("click", () => {
    alert("Our AI Portfolio Assistant will be implemented in Phase 05.");
});

checkBackend();
