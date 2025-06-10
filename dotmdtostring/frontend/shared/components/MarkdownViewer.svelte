<script lang="ts">
    import { marked } from "marked";

    export let markdownText: string = "";

    let renderedHtml: string | Promise<string> = "";

    $: if (markdownText) {
        renderedHtml = marked(markdownText);
    }

    let showMarkdownText = true
</script>



<button class="button" on:click={() => showMarkdownText = !showMarkdownText}>
    {showMarkdownText ? "Hide Text" : "Show Text"}
</button>
{#if showMarkdownText}
    <div class="scrollable-content">
        {#if markdownText}
        {#await renderedHtml then html}
            {@html html}
        {/await}
        {:else}
            <p style="text-align: center;">The Extracted Markdown Will Appear Here</p>
        {/if}
    </div>
{/if}

<style>
.scrollable-content {
    max-height: 350px;
    overflow-y: auto;
    border: 1px solid #e5e7eb; /* light gray */
    border-radius: 0.5rem;
    padding: 1rem;
    background: #fafbfc;
    font-family: inherit;
    font-size: 1rem;
    color: #222;
    box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    transition: box-shadow 0.2s;
    margin-top: 1rem;
}
.scrollable-content:focus-within, .scrollable-content:hover {
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    border-color: #b6bbc4;
}

.button {
    font-size: 0.7rem;
    padding: 2px 8px;
    border-radius: 4px;
    border: 1px solid #bbb;
    background: #f5f5f5;
    cursor: pointer;
    margin-top: 0.5rem;
}
</style>