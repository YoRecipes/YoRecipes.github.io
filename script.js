const darkThemeButton = document.getElementById("dark-theme");
const lightThemeButton = document.getElementById("light-theme");

function lightTheme() {
  document.body.classList.remove("dark-mode");
  darkThemeButton.style.display = "inline-block";
  lightThemeButton.style.display = "none";
  localStorage.setItem("theme", "light");
}
function darkTheme() {
  document.body.classList.add("dark-mode");
  darkThemeButton.style.display = "none";
  lightThemeButton.style.display = "inline-block";
  localStorage.setItem("theme", "dark");
}
darkThemeButton.addEventListener("click", darkTheme);
lightThemeButton.addEventListener("click", lightTheme);

// get theme from local storage
const localTheme = localStorage.getItem("theme");
if (localTheme === "dark") {
  darkTheme();
} else {
  lightTheme();
}
// get parameter from URL
const urlParams = new URLSearchParams(window.location.search);
const theme = urlParams.get("theme");
if (theme === "dark") {
  darkTheme();
} else if (theme === "light") {
  lightTheme();
}