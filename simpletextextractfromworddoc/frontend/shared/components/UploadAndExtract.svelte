<script lang="ts">
    import WordUploadFromDevice from "./WordUploadFromDevice.svelte";
    import WordUploadFromURL from "./WordUploadFromURL.svelte";

    let uploadMode: 'device' | 'url' = 'device'
</script>

<div class="upload-mode-selector">
    <button class="upload-mode-button {uploadMode === 'device' ? 'active' : ''}" on:click={() => uploadMode = 'device'}>Upload from Device</button>
    <button class="upload-mode-button {uploadMode === 'url' ? 'active' : ''}" on:click={() => uploadMode = 'url'}>Upload from URL</button>
</div>

{#if uploadMode === "device"}
    <WordUploadFromDevice on:upload />
{:else}
    <WordUploadFromURL on:upload />
{/if}

<style>
    .upload-mode-selector {
        display: flex;
        gap: 1rem;
        margin-top: 1rem;
        margin-bottom: 1rem;
        justify-content: center;
    }
    .upload-mode-button {
        padding: 0.5rem 1rem;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        background-color: #fafbfc;
        cursor: pointer;
        color: #222;
        font-size: 1rem;
        font-weight: 500;
        transition: background-color 0.2s, color 0.2s;
        &:hover {
            background-color: #e5e7eb;
        }
    }
    .upload-mode-button.active {
        background-color: #3b82f6;
        color: #fff;
        border-color: #3b82f6;
        font-weight: 600;
    }
</style>