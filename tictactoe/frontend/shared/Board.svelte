<script>
       import Tile from "./Tile.svelte";
</script>

<style>
	.board {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		grid-template-rows: repeat(3, 1fr);
		gap: 8px;
		width: 200px;
		height: 200px;
	}
</style>

<div class="board">
	{#each Array(9) as _, i}
		<Tile id={i} />
	{/each}
</div>
