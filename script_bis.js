function lightTheme() {
  document.body.classList.remove("dark-mode");
}
function darkTheme() {
  document.body.classList.add("dark-mode");
}

// get parameter from URL
const urlParams = new URLSearchParams(window.location.search);
const theme = urlParams.get("theme");
if (theme == "dark") {
  darkTheme();
} else if (theme == "light") {
  lightTheme();
}
