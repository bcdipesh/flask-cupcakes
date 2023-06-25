'use strict';

const BASE_URL = 'http://localhost:5000/api';

const generateCupcakeHTML = (cupcake) => `<div data-cupcake-id=${cupcake.id}>
        <li>
        <img src="${cupcake.image}" class="img-thumbnail" alt="${cupcake.flavor}" width="200">
            ${cupcake.flavor} | ${cupcake.size} | ${cupcake.rating}
            <button class="btn btn-danger">X</button>
        </li>
    </div>`;

const displayCupcakes = async () => {
	const response = await axios.get(`${BASE_URL}/cupcakes`);

	for (let data of response.data.cupcakes) {
		let cupcake = $(generateCupcakeHTML(data));
		$('#cupcakes-list').append(cupcake);
	}
};

$('#add-cupcake-form').on('submit', async (e) => {
	e.preventDefault();

	let flavor = $('#flavor').val();
	let size = $('#size').val();
	let rating = $('#rating').val();
	let image = $('#image').val();

	let response = await axios.post(`${BASE_URL}/cupcakes`, {
		flavor,
		size,
		rating,
		image,
	});

	let cupcakeHTML = $(generateCupcakeHTML(response.data.cupcake));
	$('#cupcakes-list').append(cupcakeHTML);
	$('#add-cupcake-form').trigger('reset');
});

$('#cupcakes-list').on('click', '.btn-danger', async (e) => {
	e.preventDefault();
	let cupcake = $(e.target).closest('div');
	let cupcakeId = cupcake.attr('data-cupcake-id');

	await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
	cupcake.remove();
});

$(displayCupcakes);
