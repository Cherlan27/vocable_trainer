"use client";

import "./card.css";

type CardProps = {
    word: string;
    tags?: string[];
}

export default function Card(
    { word, tags }: CardProps

) {

    return (
        <div className="card">
        <h2>{word}</h2>
        {tags && tags.length > 0 && (
            <div className="tags">
                {tags.map((tag, index) => (
                    <span key={index} className="tag">{tag}</span>
                ))}
            </div>
        )}
        </div>
    );
}