<script>
	import { fade } from 'svelte/transition';
	import { page } from './store.js';

	let serviceName = '';

	function add_service() {
		fetch('/api/services', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				service_name: serviceName
			})
		})
			.then((response) => response.json())
			.then((data) => {
				console.log(data);
				$page = 'services';
			});
	}
</script>

<div in:fade>
	<h3><u>Add new service</u></h3>
	<div class="ui form">
		<div class="field">
			<label for="">Service Name</label>
			<input type="text" bind:value={serviceName} placeholder="Service Name" />
		</div>
		<button class="ui button" on:click={add_service}>Add</button>
	</div>
</div>
