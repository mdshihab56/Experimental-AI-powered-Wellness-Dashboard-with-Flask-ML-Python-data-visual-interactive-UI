let sidebarOpen = false;
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  if (!sidebarOpen) {
    sidebar.style.left = "0";
    sidebarOpen = true;
  } else {
    sidebar.style.left = "-280px";
    sidebarOpen = false;
  }
}
async function analyze() {
  const sleep = document.getElementById("sleep").value;
  const stress = document.getElementById("stress").value;
  const productivity = document.getElementById("productivity").value;
  const water = document.getElementById("water").value;
  const screen = document.getElementById("screen").value;
  const exercise = document.getElementById("exercise").value;
  const moodText = document.getElementById("moodText").value;
  const response = await fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      sleep,
      stress,
      productivity,
      water,
      screen,
      exercise,
      moodText,
    }),
  });
  const data = await response.json();
  const result = document.getElementById("result");
  result.innerHTML = "AI Wellness Status: " + data.result;
  document.getElementById("chart").src =
    "/static/chart.png?" + new Date().getTime();
}
function toggleDarkMode() {
  document.body.classList.toggle("light");
}
function changeAccent(color) {
  document.documentElement.style.setProperty("--accent", color);
}
function toggleAnimation(element) {
  const blobs = document.querySelectorAll(".blob");
  blobs.forEach((blob) => {
    blob.style.animation = element.checked
      ? "moveBlob 10s infinite alternate"
      : "none";
  });
}
