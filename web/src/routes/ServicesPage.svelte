<script>
	import { fade } from 'svelte/transition';
	import { page, service } from './store.js';

	let fetching = false;
	let error = null;

	$: serviceList = [];
	const fetchServices = () => {
		fetching = true;
		fetch('/api/services')
			.then((data) => data.json())
			.then((data) => {
				serviceList = data;
				fetching = false;
			});
	};

	function addServicePage() {
		$page = 'addService';
	}

	function singleServicePage(serviceName) {
		$page = 'singleService';
		$service = serviceName;
	}

	function deleteService(serviceName) {
		if (confirm(`Are you sure you want to delete this service: ${serviceName}?`)) {
			fetch('/api/services/' + serviceName, {
				method: 'DELETE'
			})
				.then((response) => response.json())
				.then((data) => {
					if (data.status == 'error') {
						error = data.message;
						setTimeout(() => {
							error = null;
						}, 5000);
						console.log(data.message);
					}
					fetchServices();
				});
		}
	}

	fetchServices();
</script>

<div in:fade>
	<h2 class="ui header">Services</h2>

	<div class="ui relaxed divided list">
		{#each serviceList as service}
			<div class="item">
				<div class="right floated content">
					<button class="ui mini button" on:click={() => deleteService(service.service_name)}>
						Delete
					</button>
				</div>
				<i class="large middle aligned icon">⚙️</i>
				<div class="content">
					<button class="header" on:click={() => singleServicePage(service.service_name)}>
						{service.service_name}
					</button>
					<div class="description">{service.key_count} key(s)</div>
				</div>
			</div>
		{/each}
	</div>
	<button class="ui right floated right labeled icon mini button" on:click={addServicePage}>
		<i class="right plus icon" />
		Add Service
	</button>
	<div style="margin-top: 60px;">
		{#if error}
			<div in:fade class="ui negative message {error ? '' : 'hidden'}">
				<div class="header">Cannot delete!</div>
				<p>{error}</p>
			</div>
		{/if}
	</div>
</div>
