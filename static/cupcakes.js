function loadCupcakes() {
    axios.get('/api/cupcakes')
        .then(response => {
            const cupcakes = response.data.cupcakes;
            const cupcakeList = $('#cupcake-list');
            cupcakeList.empty();
            cupcakes.forEach(cupcake => {
                cupcakeList.append(`<li>${cupcake.flavor} - Rating: ${cupcake.rating}</li>`);
            });
        })
        .catch(error => {
            console.error(error);
        });
}

// Event with anonymous function to handle form submission and create a new cupcake
$('#cupcake-form').submit(function (event) {
    event.preventDefault();

    const flavor = $('#flavor').val();
    const size = $('#size').val();
    const rating = $('#rating').val();
    const image = $('#image').val();

    axios.post('/api/cupcakes', {
        flavor: flavor,
        size: size,
        rating: rating,
        image: image
    },
    )
    .then(response => {
        loadCupcakes(); 
        $('#cupcake-form')[0].reset(); 
    })
    .catch(error => {
        console.error(error);
    });
});

loadCupcakes();