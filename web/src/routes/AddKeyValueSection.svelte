<script>
	import { fade } from 'svelte/transition';
	import { service } from './store.js';

	export let section;

	let key = '';
	let value = '';

	function addKeyValue() {
		if (key.length > 0 && value.length > 0) {
			fetch('/api/services/' + $service + '/kv', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ key, value })
			})
				.then((res) => res.json())
				.then(() => {
					section = 'keyValue';
				});
		}
	}
</script>

<div in:fade>
	<h3><u>Add Key Value</u></h3>
	<div class="ui form">
		<div class="field">
			<label for="">Key</label>
			<input type="text" bind:value={key} placeholder="Key" />
		</div>
		<div class="field">
			<label for="">Value</label>
			<input type="text" bind:value placeholder="Value" />
		</div>
		<button class="ui button" on:click={addKeyValue}>Add</button>
	</div>
</div>
