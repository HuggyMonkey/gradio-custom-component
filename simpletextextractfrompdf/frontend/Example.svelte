<script lang="ts">
	import UploadAndExtract from "./shared/components/UploadAndExtract.svelte";
	import PDFviewer from "./shared/components/PDFviewer.svelte";
	import TextContentViewer from "./shared/components/TextContentViewer.svelte";
	

	export let value: string;
    export let type: "gallery" | "table";
    export let selected = false;

	let file: File | null = null

	
	function handleUpload(event: CustomEvent<{content: {asString: string, asFile: File}, type: string}>) {
		let {content: {asString, asFile }} = event.detail

		value = asString
		file = asFile
	}
</script>

<div
	class:table={type === "table"}
	class:gallery={type === "gallery"}
	class:selected
>

	<UploadAndExtract on:upload={handleUpload} />
	<PDFviewer bind:file/>
	<TextContentViewer bind:textContent={value}/>

</div>

<style>
	.gallery {
		padding: var(--size-1) var(--size-2);
	}
</style>
