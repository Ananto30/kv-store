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
    <button
      class={section == "keyValue" ? "active item link" : "item link"}
      on:click={() => (section = "keyValue")}
    >
      🗃️ Key Values
    </button>
    <button
      class={section == "codeGen" ? "active item link" : "item link"}
      on:click={() => (section = "codeGen")}
      >🛠️ Generate Code
    </button>
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
      bind:value={updateValue}
    />
  {/if}
</div>
