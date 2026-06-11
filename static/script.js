const fileInput = document.getElementById("file_input");
const fileLabel = document.getElementById("file_label");

fileInput.addEventListener("change", () => {
  if (fileInput.files.length > 0) {
    fileLabel.textContent = fileInput.files[0].name;
  }
});

function runDiagnosis() {
  const file = fileInput.files[0];
  const machineName = document.getElementById("machine_name").value.trim();
  const extraContext = document.getElementById("extra_context").value.trim();
  const btn = document.getElementById("diagnose_btn");
  const outputSection = document.getElementById("output_section");
  const outputBox = document.getElementById("output_box");

  if (!file) {
    alert("Please upload a file first.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);
  formData.append("machine_name", machineName);
  formData.append("extra_context", extraContext);

  btn.disabled = true;
  btn.textContent = "Diagnosing...";
  outputBox.textContent = "";
  outputSection.style.display = "block";

  fetch("/diagnose", {
    method: "POST",
    body: formData
  }).then(response => {
    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    function read() {
      reader.read().then(({ done, value }) => {
        if (done) {
          btn.disabled = false;
          btn.textContent = "Run Diagnosis";
          return;
        }

        const chunk = decoder.decode(value);
        const lines = chunk.split("\n");

        lines.forEach(line => {
          if (line.startsWith("data: ")) {
            const text = line.slice(6);
            if (text === "[DONE]") {
              btn.disabled = false;
              btn.textContent = "Run Diagnosis";
              return;
            }
            outputBox.textContent += text;
            outputBox.scrollTop = outputBox.scrollHeight;
          }
        });

        read();
      });
    }

    read();
  }).catch(() => {
    outputBox.textContent = "An error occurred. Please try again.";
    btn.disabled = false;
    btn.textContent = "Run Diagnosis";
  });
}