<script lang="ts">
 
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

   let url: string = ""

   let selectedFile: File | null = null
   let selectedFileText: string = ""
   let errorMessage: string = ""
   let fileName = ""

   let fetching = false
   let progessStatus = ""

  
    async function fetchWordDoc() {
        fetching = true;
        selectedFile = null;
        errorMessage = "";

        if (!url) {
            fetching = false;
            errorMessage = "Please enter a valid URL";
            return;
        }

        try {
            const response = await fetch(url);

            if (!response.ok) {
                fetching = false;
                errorMessage = `Failed to fetch Word Document: ${response.status}`;
                return;
            }

            const blob = await response.blob();

            if (blob.size === 0) {
                fetching = false;
                errorMessage = "The url you provided did not return a Word Document. Please check the URL and try again.";
                return;
            }

            if (blob.type !== "application/vnd.openxmlformats-officedocument.wordprocessingml.document") {
                fetching = false;
                errorMessage = "The url you provided did not return a Word Document. Please check the URL and try again.";
                return;
            }

            selectedFile = new File([blob], "downloaded.docx", { type: blob.type });
            fileName = selectedFile.name;

            fetching = false;
            errorMessage = "";
        } catch (err) {
            fetching = false;
            //TypeError in the browser
            if (err instanceof TypeError) {
                errorMessage = "An error occured fetching the file. Please check the URL and try again.";
            } else {
                errorMessage = "Oh no. Something went wrong. Please refresh the page and try again or a different URL.";
            }
        }
    }


    async function dispatchUpload(){

        progessStatus = "Checking file..."

        if (!selectedFile) {
            errorMessage = "No file selected. Please select a file to upload."
            return;
        }

        progessStatus = "Extracting text..."

        selectedFileText = await extractTextFromDocx(selectedFile);

         // check if text was extracted or file is empty
         if (selectedFile && selectedFileText.length === 0) {
            progessStatus = ""
            selectedFile = null
            errorMessage = "No text found in the file. Please select a different file."
            return
        }

        progessStatus = "Text extracted successfully"

        dispatch("upload", {selectedFilesText: selectedFileText})
    }


    async function extractTextFromDocx(file: File): Promise<string> {
        const arrayBuffer = await file.arrayBuffer();
        const { value: text } = await mammoth.extractRawText({ arrayBuffer });
        return text
    }

</script>



<div class="upload-url-container">
    <input type="url" bind:value={url} class="url-input" placeholder="Enter Word Document URL..." />
    <button class="get-pdf-button" on:click={() => fetchWordDoc()}>Get Word Document</button>
    {#if fileName}
        <p class="file-name">{fileName}</p>
    {/if}
    {#if fetching}
        <p class="fetching-message">Fetching Word Document...</p>
    {/if}
    {#if errorMessage}
        <p class="error-message">{errorMessage}</p>
    {/if}
    {#if progessStatus}
        <p class="progess-status">{progessStatus}</p>
    {/if}

</div>

{#if selectedFile}
<!-- Action Buttons -->
<div class="action-buttons">
    <button 
        class="cancel-button"
        on:click={() => {
            selectedFile = null
            fileName = ""
            errorMessage = ""
        }}
    >
        Cancel
    </button>
    <button 
        class="upload-button"
        on:click={dispatchUpload}
    >
       Upload and Extract Text
    </button>
</div>
{/if}


<style>
.upload-url-container {
    border-width: 2px;
    border-style: dashed;
    border-color: #d1d5db; /* gray-300 */
    border-radius: 0.5rem;
    padding: 2rem;
    text-align: center;
    margin-bottom: 1rem;
}
.url-input {
    width: 100%;
    max-width: 400px;
    padding: 0.5rem 1rem;
    border: 1px solid #d1d5db;
    border-radius: 0.375rem;
    font-size: 1rem;
    margin-bottom: 1rem;
    outline: none;
    transition: border-color 0.2s;
}
.url-input:focus {
    border-color: #3b82f6; /* blue-500 */
}
.get-pdf-button {
    padding: 0.5rem 1rem;
    color: #ffffff;
    background-color: #3b82f6;
    border-radius: 0.5rem;
    border: none;
    font-size: 1rem;
    margin-left: 0.5rem;
    cursor: pointer;
    transition: background 0.2s;
}
.get-pdf-button:hover {
    background-color: #2563eb;
}
.file-name {
    font-size: 0.875rem;
    line-height: 1.25rem;
    color: #3b82f6; /* blue-500 */
    margin-top: 0.5rem;
}
.error-message {
    font-size: 0.875rem;
    line-height: 1.25rem;
    color: #ef4444; /* red-500 */
    margin-top: 0.5rem;
}
.fetching-message {
    font-size: 0.875rem;
    line-height: 1.25rem;
    color: #10b981; /* emerald-500 */
    margin-top: 0.5rem;
}
.action-buttons {
    display: flex;
    justify-content: flex-end;
    margin-top: 0.5rem;
    gap: 1rem;
}
.cancel-button {
    padding: 0.5rem 1rem;
    color: #374151; /* gray-700 */
    background-color: #e5e7eb; /* gray-200 */
    border-radius: 0.5rem;
    border: none;
}
.cancel-button:hover {
    background-color: #d1d5db; /* gray-300 */
}
.cancel-button:focus {
    outline: 2px solid transparent;
    outline-offset: 2px;
    box-shadow: 0 0 0 2px #6b7281; /* ring-gray-500 */
}
.upload-button {
    padding: 0.5rem 1rem;
    color: #ffffff; /* white */
    background-color: #3b82f6; /* blue-500 */
    border-radius: 0.5rem;
    border: none;
}
.upload-button:hover {
    background-color: #2563eb; /* blue-600 */
    cursor: pointer;
}
.upload-button:focus {
    outline: 2px solid transparent;
    outline-offset: 2px;
    box-shadow: 0 0 0 2px #3b82f6; /* ring-blue-500 */
}
.progess-status {
    font-size: 0.875rem;
    line-height: 1.25rem;
    color: #10b981; /* emerald-500 */
}
</style>