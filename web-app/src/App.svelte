<script>
  import AddServicePage from "./AddServicePage.svelte";
  import SingleServicePage from "./SingleServicePage.svelte";
  import ServicesPage from "./ServicesPage.svelte";
  import ConnectPage from "./ConnectPage.svelte";

  import { onMount } from "svelte";

  import { page, needConnect, host, port, db } from "./store.js";

  const fetchInit = () => {
    fetch("/api/init")
      .then((data) => data.json())
      .then((data) => {
        if (data.need_connect) {
          $needConnect = true;
          $page = "connect";
        } else {
          $needConnect = false;
          $host = data.host;
          $port = data.port;
          $db = data.db;
        }
      });
  };

  function servicesPage() {
    if ($needConnect) {
      $page = "connect";
    } else {
      $page = "services";
    }
  }

  onMount(() => {
    fetchInit();
  });
</script>

<main>
  <div class="container">
    <div class="ui secondary pointing menu">
      <h2>🗄️ KV Store</h2>
      <div class="right menu">
        <button
          class={$page == "services" ? "active item link" : "item link"}
          on:click={servicesPage}
        >
          ⚙️ Services
        </button>

        <button
          class={$page == "connect" ? "active item link" : "item link"}
          on:click={() => ($page = "connect")}>🔗 Connect</button
        >
      </div>
    </div>

    {#if $page == "services"}
      <ServicesPage />
    {:else if $page == "addService"}
      <AddServicePage />
    {:else if $page == "singleService"}
      <SingleServicePage />
    {:else if $page == "connect"}
      <ConnectPage />
    {/if}
  </div>
</main>
