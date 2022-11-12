console.log("Welcome to our application")

const searchInput = document.getElementById("searchMovie");
const movieContainer = document.querySelector(".container");

// Request OMDB API

searchInput.addEventListener("input",fetchData);

function fetchData(){
    fetch(`https://www.omdbapi.com/?i=tt3896198&apikey=44df4b43&s=${searchInput.value}`)  //Promise Generated
    .then(response=>response.json())
    .then((response)=>{
        console.log(response['Search']);

        displayMovies(response['Search']);
    })
    .catch(err=>console.log("Error: ",err));
}

function displayMovies(movies){

    let html = "";

    movies.forEach((element,index) => {
        console.log("Index: ");
        console.log(index);

        console.log("Element ");
        console.log(element);


        html += `
                    <div class="movie">
                        <img src="${element.Poster}" alt="">
                        <h3>${element.Title}</h3>
                        <p>${element.Year}</p> 
                        
                        
                        <button><a href="/details.html?id=${element.imdbID}">View More</button>
                    </div>
                `;

    });

    movieContainer.innerHTML = html;
}