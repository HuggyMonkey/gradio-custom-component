<script lang="ts">
	import WordUpload from "./shared/components/WordUpload.svelte";
	import TextContentViewer from "./shared/components/TextContentViewer.svelte";

	export let value: string;
	export let type: "gallery" | "table";
	export let selected = false;
</script>

<div
	class:table={type === "table"}
	class:gallery={type === "gallery"}
	class:selected
>
	<WordUpload/>
	<TextContentViewer textContent={value}/>
</div>

<style>
	.gallery {
		padding: var(--size-1) var(--size-2);
	}
</style>
