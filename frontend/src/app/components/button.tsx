"use client";

import './button.css';

type ButtonProps = {
    title: string;
    onClickButton?: () => void;
}

export default function MyButton(
    { title, onClickButton }: ButtonProps
) {
    return (
        <button className="my-button" onClick={onClickButton}>{title}</button>
    )
}