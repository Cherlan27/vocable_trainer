"use client";

import { useRouter } from 'next/navigation';
import { useState } from "react";
import { MyButton, MyButton2 } from "@/app/components/button";
import InputField from "@/app/components/input";
import VocTable from "@/app/components/voc_table";
import { Vocable } from "@/app/schemas/vocables";
import styles from "../../page.module.css";
import "./page_style.css";


export default function Cards() {
  const router = useRouter();

  const [vocable, setVocable] = useState<Vocable[]>([]);
  const [topic, setTopic] = useState<string>("");
  const height = vocable.length === 0 ? "100px" : "300px";

  function generateVocables(topicValue : string) {
    console.log("New vocables generated");
    fetch(process.env.NEXT_PUBLIC_BACKEND_URL + '/generate/new_vocables', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
    },
      body: JSON.stringify({ topic: topicValue }),
    })
      .then(response => {
        console.log(response);
        if (response.ok) {
          return response.json()
        }
      })
      .then(data => {
        console.log(data);
        setVocable(data.vocables);
        console.log("here are the vocables: ", data.vocables);
      })
      .catch(error => {
        setVocable([]);
      });
  }

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div className="container">
          <h1>Cards Page</h1>
          <p>Learn new vocables in an easy way!</p>
          <div style={{
            height: '40px',
            width: '100%',
            marginBottom: '30px',
            marginTop: '10px',
            display: 'flex',
            flexDirection: 'row',
            gap: '10px',
            alignItems: 'center',
            justifyContent: 'center',
          }}>
            <InputField value={topic} onInputChange={setTopic} id="Input-Topic"/>
            <MyButton2 title="Process" onClickButton={() => generateVocables(topic)} id="Input-Button"/>
          </div>
          <div>
            <div
              style={{
                height,
                overflowY: 'auto',
                width: '100%',
                marginBottom: '20px',
                justifyContent: 'center',
                display: 'flex',
                transition: "height 1s ease"
              }}
            >
              {vocable.length === 0 ? (
                <p>Wait for new vocables...</p>
              ) : (
                <VocTable vocList={vocable} />
              )}
            </div>
          </div>
          <div style ={{ marginBottom: '20px', width : '100%', display: 'flex', justifyContent: 'center' }}>
            {
              vocable.length > 0 ? <MyButton title="Saving vocables" onClickButton={() => router.push('/')} /> : null
            }
          </div>
          <MyButton title="Back to Home" onClickButton={() => router.push('/')} />
        </div>
      </main>
    </div>
  );
}
