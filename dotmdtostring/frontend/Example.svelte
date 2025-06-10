<script lang="ts">
	import MarkdownViewer from "./shared/components/MarkdownViewer.svelte";
	import UploadAndExtract from "./shared/components/UploadAndExtract.svelte";

	export let value: string;
	export let type: "gallery" | "table";
	export let selected = false;

	function handleUpload(event: CustomEvent<{ selectedFilesText: string }>) {
		value = event.detail.selectedFilesText;
	}
</script>

<div
	class:table={type === "table"}
	class:gallery={type === "gallery"}
	class:selected
>
	<UploadAndExtract on:upload={handleUpload} />
	<MarkdownViewer bind:markdownText={value} />

	<p class="value-status">{value ? "Value is set ✅" : "Value is not set ❌"}</p>
</div>

<style>
	.gallery {
		padding: var(--size-1) var(--size-2);
	}
</style>
