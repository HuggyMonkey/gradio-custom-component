<script lang="ts">
	import MarkdownViewer from "./shared/components/MarkdownViewer.svelte";
	import MarkdownUpload from "./shared/components/MarkdownUpload.svelte";

	export let value: string;
	export let type: "gallery" | "table";
	export let selected = false;
</script>

<div
	class:table={type === "table"}
	class:gallery={type === "gallery"}
	class:selected
>
	<MarkdownUpload />
	<MarkdownViewer bind:markdownText={value} />

	<p class="value-status">{value ? "Value is set ✅" : "Value is not set ❌"}</p>
</div>

<style>
	.gallery {
		padding: var(--size-1) var(--size-2);
	}
</style>
