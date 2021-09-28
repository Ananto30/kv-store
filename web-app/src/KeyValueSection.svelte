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
    fetch("/api/services/" + $service)
      .then((data) => data.json())
      .then((data) => {
        keyVals = data.key_values;
        fetching = false;
      });
  };

  function deleteKeyVal(key) {
    if (confirm(`Are you sure you want to delete this key: ${key}?`)) {
      fetch("/api/services/" + $service + "/kv/" + key, {
        method: "DELETE",
      }).then(() => {
        fetchServiceKeyVals();
      });
    }
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
        <th class="three wide">Delete / Update</th>
      </tr>
    </thead>
    <tbody>
      {#each Object.entries(keyVals) as [key, value]}
        <tr>
          <td>{key}</td>
          <td>{value}</td>
          <td class="">
            <button class="ui mini button" on:click={() => deleteKeyVal(key)}
              >❌</button
            >
            <button
              class="ui mini button"
              on:click={() => updateKeyValSection(key, value)}>🔧</button
            >
          </td>
        </tr>
      {/each}
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
