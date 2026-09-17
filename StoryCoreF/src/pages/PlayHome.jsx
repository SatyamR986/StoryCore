import { useEffect, useState } from "react";
import { getStories } from "../api/storyApi";
import StoryCard from "../components/play/StoryCard";

export default function PlayHome() {
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchStories() {
      try {
        const data = await getStories();
        setStories(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchStories();
  }, []);

  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <div className="mx-auto max-w-5xl px-6 py-12">

        <header className="mb-12">
          <h1 className="text-5xl font-bold tracking-tight">
            StoryCore
          </h1>

          <p className="mt-3 text-lg text-zinc-400">
            Choose your next adventure.
          </p>
        </header>

        {loading && (
          <p className="text-zinc-400">
            Loading stories...
          </p>
        )}

        {error && (
          <p className="text-red-400">
            {error}
          </p>
        )}

        {!loading && !error && (
          <div className="space-y-6">
            {stories.map((story) => (
              <StoryCard
                key={story.id}
                story={story}
              />
            ))}
          </div>
        )}

      </div>
    </main>
  );
}