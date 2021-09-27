<script>
  import AddServicePage from "./AddServicePage.svelte";
  import SingleServicePage from "./SingleServicePage.svelte";
  import ServicesPage from "./ServicesPage.svelte";

  import { page } from "./store.js";

  function servicePage() {
    $page = "services";
  }
</script>

<main>
  <div class="container">
    <div class="ui secondary pointing menu">
      <h2>🗄️ KV Store</h2>
      <div class="right menu">
        <a
          class={$page == "services" ? "active item" : "item"}
          on:click={servicePage}
        >
          Services
        </a>

        <a class="item"> Connect </a>
      </div>
    </div>

    {#if $page == "services"}
      <ServicesPage />
    {:else if $page == "addService"}
      <AddServicePage />
    {:else if $page == "singleService"}
      <SingleServicePage />
    {/if}
  </div>
</main>
