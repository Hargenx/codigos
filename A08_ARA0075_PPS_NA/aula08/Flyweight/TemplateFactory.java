package A08_ARA0075_PPS_NA.aula08.Flyweight;

import java.util.HashMap;
import java.util.Map;

public class TemplateFactory {
    private Map<String, TemplateHTML> templates = new HashMap<>();

    public EmailTemplate getTemplate(String layout) {
        templates.putIfAbsent(layout, new TemplateHTML(layout));
        return templates.get(layout);
    }
}
