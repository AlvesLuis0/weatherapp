const searchInput = document.getElementById("search-input");
const searchButton = document.getElementById("search-button");

async function searchCity(event) {
  if(event.key == "Enter" && searchInput.value)
    location.assign(`/${searchInput.value}`);
}

searchInput.addEventListener("keydown", searchCity);
searchButton.addEventListener("click", async() => searchCity({ "key": "Enter" }));