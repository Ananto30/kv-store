<script>
  import { fade } from "svelte/transition";
  import { service } from "./store.js";

  export let section;

  export let key;
  export let val;

  function addKeyValue() {
    if (key.length > 0 && val.length > 0) {
      fetch("http://localhost:5000/api/services/" + $service + "/kv", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ key, val }),
      })
        .then((res) => res.json())
        .then((res) => {
          section = "keyValue";
        });
    }
  }
</script>

<div in:fade>
  <h3><u>Update Key Value</u></h3>
  <div class="ui form">
    <div class="disabled field">
      <label>Key</label>
      <input type="text" bind:value={key} placeholder="Key" />
    </div>
    <div class="field">
      <label>Value</label>
      <input type="text" bind:value={val} placeholder="Value" />
    </div>
    <button class="ui button" on:click={addKeyValue}>Update</button>
  </div>
</div>
