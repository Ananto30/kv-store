<script>
  import { fade } from "svelte/transition";
  import { service } from "./store.js";

  $: code = "";

  function fetchCode(language) {
    code = "";
    fetch(
      "/api/services/" +
        $service +
        "/generate_code/" +
        language
    )
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        code = data;
      });
  }
</script>

<div in:fade>
  <button class="ui mini button" on:click={() => fetchCode("python")}
    >Python</button
  >
  <button class="ui mini button" on:click={() => fetchCode("java")}>Java</button
  >

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
