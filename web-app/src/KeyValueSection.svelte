<script>
  import { fade } from "svelte/transition";
  import { service } from "./store.js";
  import { onMount } from "svelte";

  export let section;
  export let updateKey;
  export let updateValue;
  let fetching = false;
  $: keyVals = new Map();

  const fetchServiceKeyVals = () => {
    fetching = true;
    fetch("http://localhost:5000/api/services/" + $service)
      .then((data) => data.json())
      .then((data) => {
        console.log(data.key_values);
        keyVals = data.key_values;
        fetching = false;
      });
  };

  function deleteKeyVal(key) {
    fetch("http://localhost:5000/api/services/" + $service + "/kv/" + key, {
      method: "DELETE",
    }).then(() => {
      fetchServiceKeyVals();
    });
  }

  function updateKeyValSection(key, value) {
    updateKey = key;
    updateValue = value;
    section = "updateKeyVal";
  }

  onMount(() => {
    fetchServiceKeyVals();
  });
</script>

<div in:fade>
  <table class="ui fixed selectable celled table">
    <thead>
      <tr>
        <th>🗝️ Key</th>
        <th>🔐 Value</th>
        <th class="three wide" />
      </tr>
    </thead>
    <tbody>
      {#if fetching}
        <div class="ui placeholder">
          <div class="line" />
          <div class="line" />
          <div class="line" />
          <div class="line" />
          <div class="line" />
        </div>
      {:else}
        {#each Object.entries(keyVals) as [key, val]}
          <tr>
            <td>{key}</td>
            <td>{val}</td>
            <td class="">
              <button class="ui mini button" on:click={() => deleteKeyVal(key)}
                >❌</button
              >
              <button
                class="ui mini button"
                on:click={() => updateKeyValSection(key, val)}>🔧</button
              >
            </td>
          </tr>
        {/each}
      {/if}
    </tbody>
    <tfoot class="full-width">
      <tr>
        <th colspan="3">
          <button
            class="ui right floated right labeled icon mini button"
            on:click={() => (section = "addKeyValue")}
          >
            <i class="right plus icon" />
            Add Key Value
          </button>
        </th>
      </tr>
    </tfoot>
  </table>
</div>
