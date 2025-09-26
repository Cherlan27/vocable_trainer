"use client";

import "./card_translated.css";

type CardProps = {
    word: string;
}

export default function CardTranslated(
    { word }: CardProps
) {

    return (
        <div className="card">
        <h2>Vocable</h2>
        <p>{word}</p>
        </div>
    );
}