const BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function getStories() {
    const response = await fetch(`${BASE_URL}/stories/`);

    if (!response.ok) {
        throw new Error("Failed to fetch stories.");
    }

    const stories = await response.json();

    return stories;
}