<script>
  import { fade } from "svelte/transition";
  import { service } from "./store.js";

  $: code = "";

  function fetchPythonCode() {
    code = "";
    fetch(
      "http://localhost:5000/api/services/" + $service + "/generate_code/python"
    )
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        code = data;
      });
  }

  function fetchJavaCode() {
    code = "";
    fetch(
      "http://localhost:5000/api/services/" + $service + "/generate_code/java"
    )
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        code = data;
      });
  }
</script>

<div in:fade>
  <button class="ui mini button" on:click={fetchPythonCode}>Python</button>
  <button class="ui mini button" on:click={fetchJavaCode}>Java</button>

  {#if code}
    <div in:fade>
      <pre
        class="brush: python"
        lang="python">
         <code>{code}</code>
      </pre>
    </div>
  {/if}
</div>
