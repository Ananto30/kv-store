<script>
  import { fade } from "svelte/transition";
  import KeyValueSection from "./KeyValueSection.svelte";
  import { service } from "./store.js";
  import AddKeyValueSection from "./AddKeyValueSection.svelte";
  import CodeGenSection from "./CodeGenSection.svelte";
  import UpdateKeyValueSection from "./UpdateKeyValueSection.svelte";

  export let section = "keyValue";

  export let updateKey = "";
  export let updateValue = "";
</script>

<div in:fade>
  <h2 class="ui header">
    <i class="ui icon">⚙️</i>
    <div class="content">
      {$service}
      <div class="sub header">Service</div>
    </div>
  </h2>

  <div class="ui pointing menu">
    <a
      class={section == "keyValue" ? "active item" : "item"}
      on:click={() => (section = "keyValue")}
    >
      🗃️ Key Values
    </a>
    <a
      class={section == "codeGen" ? "active item" : "item"}
      on:click={() => (section = "codeGen")}
      >🛠️ Generate Code
    </a>
  </div>

  {#if section === "keyValue"}
    <KeyValueSection bind:section bind:updateKey bind:updateValue />
  {:else if section === "addKeyValue"}
    <AddKeyValueSection bind:section />
  {:else if section === "codeGen"}
    <CodeGenSection />
  {:else if section === "updateKeyVal"}
    <UpdateKeyValueSection
      bind:section
      bind:key={updateKey}
      bind:val={updateValue}
    />
  {/if}
</div>
