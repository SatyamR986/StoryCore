import { useNavigate } from "react-router-dom";

export default function StoryCard({ story }) {
  const navigate = useNavigate();

  return (
    <article className="group overflow-hidden rounded-2xl border border-zinc-800 bg-zinc-900 transition duration-300 hover:border-cyan-500 hover:shadow-xl hover:shadow-cyan-500/10">

      <div className="flex">

        {/* Cover */}

        <div className="flex h-48 w-36 shrink-0 items-center justify-center bg-gradient-to-br from-cyan-700 via-sky-700 to-indigo-900">

          <span className="text-5xl">
             ▷
          </span>

        </div>

        {/* Right */}

        <div className="flex flex-1 flex-col p-6">

          <h2 className="text-3xl font-semibold text-white transition group-hover:text-cyan-300">
            {story.title}
          </h2>

          <p className="mt-4 text-zinc-400 leading-7 line-clamp-3">
            {story.description || "No description available."}
          </p>

          <div className="mt-auto flex items-center justify-between pt-6">

            <span className="rounded-full border border-zinc-700 px-3 py-1 text-xs uppercase tracking-wide text-zinc-500">
              Interactive Story
            </span>

            <button
              onClick={() => navigate(`/play/${story.id}`)}
              className="rounded-xl bg-cyan-500 px-6 py-3 font-semibold text-black transition hover:bg-cyan-400"
            >
              Play →
            </button>

          </div>

        </div>

      </div>

    </article>
  );
}