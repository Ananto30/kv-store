<script>
	import { fade } from 'svelte/transition';
	import { page, host, port, db, needConnect } from './store.js';

	/**
	 * @type {?string}
	 */
	let error = null;
	let password = '';

	function connect() {
		fetch('/api/redis/connect', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				host: $host,
				port: $port,
				db: $db,
				password: password
			})
		})
			.then((res) => res.json())
			.then((res) => {
				if (res.status == 'error') {
					error = res.message;
					setTimeout(() => {
						error = null;
					}, 5000);
				} else {
					$needConnect = false;
					$page = 'services';
				}
				console.log(res);
			});
	}
</script>

<div in:fade>
	<h3><u>Add Key Value</u></h3>
	<div class="ui form">
		<div class="field">
			<label for="">Redis Host 📫 </label>
			<input type="text" bind:value={$host} placeholder="Host" />
		</div>
		<div class="field">
			<label for="">Redis Port 🔌</label>
			<input type="text" bind:value={$port} placeholder="Port" />
		</div>
		<div class="field">
			<label for="">Redis Password 🔐</label>
			<input type="password" bind:value={password} placeholder="Password" />
		</div>
		<div class="field">
			<label for="">Redis DB 🗄️</label>
			<input type="text" bind:value={$db} placeholder="DB" />
		</div>
		<button class="ui button" on:click={connect}>Connect</button>
	</div>

	<div style="margin-top: 60px;">
		{#if error}
			<div in:fade class="ui negative message {error ? '' : 'hidden'}">
				<div class="header">Cannot connect!</div>
				<p>{error}</p>
			</div>
		{/if}
	</div>
</div>
